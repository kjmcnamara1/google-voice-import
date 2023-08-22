from dataclasses import dataclass


@dataclass
class MMSPart:
    seq: int
    ct: str
    name: str
    chset: int | None = None
    cd: float | None = None
    fn: float | None = None
    cid: str
    cl: str
    ctt_s: float | None = None
    ctt_t: float | None = None
    text: str


@dataclass
class MMSAddr:
    address: str
    type: int
    charset: int


@dataclass
class MMSMessage:
    date: int
    rr: float | None = None
    sub: str | None = None
    ct_t: str | None = None
    read_status: int | None = None
    seen: int = 1
    msg_box: int
    address: str
    sub_cs: int | None = None
    resp_st: float | None = None
    retr_st: float | None = None
    d_tm: float | None = None
    text_only: int
    exp: int | None = None
    locked: int=0
    m_id: float | None = None
    st: float | None = None
    retr_txt_cs: float | None = None
    retr_txt: float | None = None
    creator: str = "com.android.providers.telephony"
    date_sent: int=0
    read: int=1
    m_size: int | None = None
    rpt_a: float | None = None
    ct_cls: float | None = None
    pri: int | None = None
    sub_id: int=-1
    tr_id: str
    resp_txt: float | None = None
    ct_l: str | None = None
    m_cls: str | None = None
    d_rpt: float | None = None
    v: float | None = None
    _id: int
    m_type: int=132
    readable_date: str
    contact_name: str ="(Unknown)"
    parts: list[MMSPart]
    addrs: list[MMSAddr]
