from dataclasses import dataclass


@dataclass
class MMSPart:
    seq:int
    ct:str
    name:str
    chset:int|None=None
    cd:
    fn:
    cid:str
    cl:str
    ctt_s:
    ctt_t:
    text:str

@dataclass
class MMSAddr:
    address:str
    type:int
    charset:int

@dataclass
class MMSMessage:
    date: int
    rr: float
    sub: str
    ct_t: str
    read_status: float
    seen: int
    msg_box: int
    address: str
    sub_cs: float
    resp_st: float
    retr_st: float
    d_tm: float
    text_only: int
    exp: float
    locked: int
    m_id: float
    st: float
    retr_txt_cs: float
    retr_txt: float
    creator: str
    date_sent: int
    read: int
    m_size: float
    rpt_a: float
    ct_cls: float
    pri: float
    sub_id: int
    tr_id: str
    resp_txt: float
    ct_l: str
    m_cls: str
    d_rpt: float
    v: float
    _id: int
    m_type: int
    readable_date: str
    contact_name: str
    parts: list[MMSPart]
    addrs: list[MMSAddr]
