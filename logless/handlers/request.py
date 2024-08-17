import logging
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from pysnmp.hlapi import *


class SplunkHandler(logging.Handler):
    def __init__(self, host, token, level: int | str = 0) -> None:
        super().__init__(level)
        self.host = host
        self.token = token

    def emit(self, record):
        log_entry = self.format(record)
        headers = {"Authorization": f"Splunk {self.token}"}
        requests.post(
            f"{self.host}/services/collector", headers=headers, data=log_entry
        )
        return super().emit(record)


class ElasticSearchHandler(logging.Handler):
    def __init__(self, host, index, level: int | str = 0) -> None:
        super().__init__(level)
        self.host = host
        self.index = index

    def emit(self, record):
        log_entry = self.format(record)
        url = f"{self.host}/{self.index}/_doc/"
        requests.post(url, json={"message": log_entry})
        return super().emit(record)


class APIHandler(logging.Handler):
    def __init__(self, endpoint, api_key, level: int | str = 0) -> None:
        super().__init__(level)
        self.endpoint = endpoint
        self.api_key = api_key

    def emit(self, record):
        log_entry = self.format(record)
        headers = {"Authorization": f"Bearer {self.api_key}"}
        requests.post(self.endpoint, headers=headers, json={"log": log_entry})
        return super().emit(record)


class SNMPHandler(logging.Handler):
    def __init__(
        self, trap_receiver, community="public", port=162, level: int | str = 0
    ) -> None:
        super().__init__(level)
        self.trap_receiver = trap_receiver
        self.community = community
        self.port = port

    def emit(self, record: logging.LogRecord) -> None:
        log_entry = self.format(record)
        errorIndication, errorStatus, errorIndex, varBinds = next(
            sendNotification(
                SnmpEngine(),
                CommunityData(self.community, mpModel=1),
                UdpTransportTarget((self.trap_receiver, self.port)),
                ContextData(),
                "trap",
                ObjectType(
                    ObjectIdentity("1.3.6.1.4.1.12345.1.1.1"), OctetString(log_entry)
                ),
            )
        )
        if errorIndication:
            print(f"SNMP Error: {errorIndication}")
        elif errorStatus:
            print(f"SNMP Error: {errorStatus.prettyPrint()}")
        return super().emit(record)


class EmailHandler(logging.Handler):
    def __init__(
        self,
        smtp_server,
        smtp_port,
        from_addr,
        to_addrs,
        subject,
        username=None,
        password=None,
        port=162,
        level: int | str = 0,
    ) -> None:
        super().__init__(level)
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_addr = from_addr
        self.to_addrs = to_addrs
        self.subject = subject
        self.username = username
        self.password = password

    def emit(self, record):
        log_entry = self.format(record)
        msg = MIMEMultipart()
        msg["From"] = self.from_addr
        msg["To"] = ", ".join(self.to_addrs)
        msg["Subject"] = self.subject
        msg.attach(MIMEText(log_entry, "plain"))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            if self.username and self.password:
                server.login(self.username, self.password)
            server.sendmail(self.from_addr, self.to_addrs, msg.as_string())
