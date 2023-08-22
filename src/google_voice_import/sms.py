from dataclasses import dataclass


@dataclass
class SMSMessage:
    protocol: int = 0
    address: str
    date: int
    type: int
    subject: str | None = None
    body: str
    toa: float | None = None
    sc_toa: float | None = None
    service_center: float | None = None
    read: int = 1
    status: int = -1
    locked: int = 0
    date_sent: int = 0
    sub_id: int = -1
    readable_date: str
    contact_name: str = "(Unknown)"
