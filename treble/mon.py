import logging
from .packet import HCICmd, HCIEvt, HCIACLData

log = logging.getLogger('treble.mon')

TX = '<'
RX = '>'

class Monitor:

    def __init__(self):
       pass

    def feed_rx(self, pkt):
        self._feed(RX, pkt)

    def feed_tx(self, pkt):
        self._feed(TX, pkt)

    def _feed(self, dir: str, pkt):
        if isinstance(pkt, bytes) or isinstance(pkt, bytearray):
            raise NotImplementedError
        elif dir == TX and isinstance(pkt, HCICmd):
            self._cmd(pkt.data)
        elif dir == RX and isinstance(pkt, HCIEvt):
            self._evt(pkt.data)
        elif isinstance(pkt, HCIACLData):
            self._acl(dir, pkt.data)
        else:
            raise NotImplementedError

    def _cmd(self, pkt: bytearray):
        pass

    def _evt(self, pkt: bytearray):
        pass

    def _acl(self, dir: str, pkt: bytearray):
        pass

