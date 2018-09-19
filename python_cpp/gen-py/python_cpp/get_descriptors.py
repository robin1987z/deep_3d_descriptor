#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    def return_descriptors(self, input):
        """
        Parameters:
         - input
        """
        pass

    def match_descriptors(self, feature_1, feature_2):
        """
        Parameters:
         - feature_1
         - feature_2
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def return_descriptors(self, input):
        """
        Parameters:
         - input
        """
        self.send_return_descriptors(input)
        return self.recv_return_descriptors()

    def send_return_descriptors(self, input):
        self._oprot.writeMessageBegin('return_descriptors', TMessageType.CALL, self._seqid)
        args = return_descriptors_args()
        args.input = input
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_return_descriptors(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = return_descriptors_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "return_descriptors failed: unknown result")

    def match_descriptors(self, feature_1, feature_2):
        """
        Parameters:
         - feature_1
         - feature_2
        """
        self.send_match_descriptors(feature_1, feature_2)
        return self.recv_match_descriptors()

    def send_match_descriptors(self, feature_1, feature_2):
        self._oprot.writeMessageBegin('match_descriptors', TMessageType.CALL, self._seqid)
        args = match_descriptors_args()
        args.feature_1 = feature_1
        args.feature_2 = feature_2
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_match_descriptors(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = match_descriptors_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        raise TApplicationException(TApplicationException.MISSING_RESULT, "match_descriptors failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["return_descriptors"] = Processor.process_return_descriptors
        self._processMap["match_descriptors"] = Processor.process_match_descriptors

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_return_descriptors(self, seqid, iprot, oprot):
        args = return_descriptors_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = return_descriptors_result()
        try:
            result.success = self._handler.return_descriptors(args.input)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("return_descriptors", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_match_descriptors(self, seqid, iprot, oprot):
        args = match_descriptors_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = match_descriptors_result()
        try:
            result.success = self._handler.match_descriptors(args.feature_1, args.feature_2)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("match_descriptors", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class return_descriptors_args(object):
    """
    Attributes:
     - input
    """


    def __init__(self, input=None,):
        self.input = input

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.input = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readDouble()
                        self.input.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('return_descriptors_args')
        if self.input is not None:
            oprot.writeFieldBegin('input', TType.LIST, 1)
            oprot.writeListBegin(TType.DOUBLE, len(self.input))
            for iter6 in self.input:
                oprot.writeDouble(iter6)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(return_descriptors_args)
return_descriptors_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'input', (TType.DOUBLE, None, False), None, ),  # 1
)


class return_descriptors_result(object):
    """
    Attributes:
     - success
    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = iprot.readDouble()
                        self.success.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('return_descriptors_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.DOUBLE, len(self.success))
            for iter13 in self.success:
                oprot.writeDouble(iter13)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(return_descriptors_result)
return_descriptors_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.DOUBLE, None, False), None, ),  # 0
)


class match_descriptors_args(object):
    """
    Attributes:
     - feature_1
     - feature_2
    """


    def __init__(self, feature_1=None, feature_2=None,):
        self.feature_1 = feature_1
        self.feature_2 = feature_2

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.feature_1 = []
                    (_etype17, _size14) = iprot.readListBegin()
                    for _i18 in range(_size14):
                        _elem19 = iprot.readDouble()
                        self.feature_1.append(_elem19)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.feature_2 = []
                    (_etype23, _size20) = iprot.readListBegin()
                    for _i24 in range(_size20):
                        _elem25 = iprot.readDouble()
                        self.feature_2.append(_elem25)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('match_descriptors_args')
        if self.feature_1 is not None:
            oprot.writeFieldBegin('feature_1', TType.LIST, 1)
            oprot.writeListBegin(TType.DOUBLE, len(self.feature_1))
            for iter26 in self.feature_1:
                oprot.writeDouble(iter26)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.feature_2 is not None:
            oprot.writeFieldBegin('feature_2', TType.LIST, 2)
            oprot.writeListBegin(TType.DOUBLE, len(self.feature_2))
            for iter27 in self.feature_2:
                oprot.writeDouble(iter27)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(match_descriptors_args)
match_descriptors_args.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'feature_1', (TType.DOUBLE, None, False), None, ),  # 1
    (2, TType.LIST, 'feature_2', (TType.DOUBLE, None, False), None, ),  # 2
)


class match_descriptors_result(object):
    """
    Attributes:
     - success
    """


    def __init__(self, success=None,):
        self.success = success

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.LIST:
                    self.success = []
                    (_etype31, _size28) = iprot.readListBegin()
                    for _i32 in range(_size28):
                        _elem33 = iprot.readI32()
                        self.success.append(_elem33)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('match_descriptors_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.LIST, 0)
            oprot.writeListBegin(TType.I32, len(self.success))
            for iter34 in self.success:
                oprot.writeI32(iter34)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(match_descriptors_result)
match_descriptors_result.thrift_spec = (
    (0, TType.LIST, 'success', (TType.I32, None, False), None, ),  # 0
)
fix_spec(all_structs)
del all_structs

