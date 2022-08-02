#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys

from thrift.transport import TTransport


class AnnotationType(object):
    BOOL = 0
    BYTES = 1
    I16 = 2
    I32 = 3
    I64 = 4
    DOUBLE = 5
    STRING = 6

    _VALUES_TO_NAMES = {
        0: "BOOL",
        1: "BYTES",
        2: "I16",
        3: "I32",
        4: "I64",
        5: "DOUBLE",
        6: "STRING",
    }

    _NAMES_TO_VALUES = {
        "BOOL": 0,
        "BYTES": 1,
        "I16": 2,
        "I32": 3,
        "I64": 4,
        "DOUBLE": 5,
        "STRING": 6,
    }


class Endpoint(object):
    """
    Indicates the network context of a service recording an annotation with two
    exceptions.

    When a BinaryAnnotation, and key is CLIENT_ADDR or SERVER_ADDR,
    the endpoint indicates the source or destination of an RPC. This exception
    allows zipkin to display network context of uninstrumented services, or
    clients such as web browsers.

    Attributes:
     - ipv4: IPv4 host address packed into 4 bytes.

    Ex for the ip 1.2.3.4, it would be (1 << 24) | (2 << 16) | (3 << 8) | 4
     - port: IPv4 port

    Note: this is to be treated as an unsigned integer, so watch for negatives.

    Conventionally, when the port isn't known, port = 0.
     - service_name: Service name in lowercase, such as "memcache" or "zipkin-web"

    Conventionally, when the service name isn't known, service_name = "unknown".
     - ipv6: IPv6 host address packed into 16 bytes. Ex Inet6Address.getBytes()
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'ipv4', None, None, ),  # 1
        (2, TType.I16, 'port', None, None, ),  # 2
        (3, TType.STRING, 'service_name', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'ipv6', 'BINARY', None, ),  # 4
    )

    def __init__(self, ipv4=None, port=None, service_name=None, ipv6=None,):
        self.ipv4 = ipv4
        self.port = port
        self.service_name = service_name
        self.ipv6 = ipv6

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.ipv4 = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I16:
                    self.port = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.service_name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.ipv6 = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Endpoint')
        if self.ipv4 is not None:
            oprot.writeFieldBegin('ipv4', TType.I32, 1)
            oprot.writeI32(self.ipv4)
            oprot.writeFieldEnd()
        if self.port is not None:
            oprot.writeFieldBegin('port', TType.I16, 2)
            oprot.writeI16(self.port)
            oprot.writeFieldEnd()
        if self.service_name is not None:
            oprot.writeFieldBegin('service_name', TType.STRING, 3)
            oprot.writeString(self.service_name.encode('utf-8') if sys.version_info[0] == 2 else self.service_name)
            oprot.writeFieldEnd()
        if self.ipv6 is not None:
            oprot.writeFieldBegin('ipv6', TType.STRING, 4)
            oprot.writeBinary(self.ipv6)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(L)})"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Annotation(object):
    """
    An annotation is similar to a log statement. It includes a host field which
    allows these events to be attributed properly, and also aggregatable.

    Attributes:
     - timestamp: Microseconds from epoch.

    This value should use the most precise value possible. For example,
    gettimeofday or syncing nanoTime against a tick of currentTimeMillis.
     - value
     - host: Always the host that recorded the event. By specifying the host you allow
    rollup of all events (such as client requests to a service) by IP address.
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I64, 'timestamp', None, None, ),  # 1
        (2, TType.STRING, 'value', 'UTF8', None, ),  # 2
        (3, TType.STRUCT, 'host', (Endpoint, Endpoint.thrift_spec), None, ),  # 3
    )

    def __init__(self, timestamp=None, value=None, host=None,):
        self.timestamp = timestamp
        self.value = value
        self.host = host

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.value = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.host = Endpoint()
                    self.host.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Annotation')
        if self.timestamp is not None:
            oprot.writeFieldBegin('timestamp', TType.I64, 1)
            oprot.writeI64(self.timestamp)
            oprot.writeFieldEnd()
        if self.value is not None:
            oprot.writeFieldBegin('value', TType.STRING, 2)
            oprot.writeString(self.value.encode('utf-8') if sys.version_info[0] == 2 else self.value)
            oprot.writeFieldEnd()
        if self.host is not None:
            oprot.writeFieldBegin('host', TType.STRUCT, 3)
            self.host.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(L)})"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class BinaryAnnotation(object):
    """
    Binary annotations are tags applied to a Span to give it context. For
    example, a binary annotation of "http.uri" could the path to a resource in a
    RPC call.

    Binary annotations of type STRING are always queryable, though more a
    historical implementation detail than a structural concern.

    Binary annotations can repeat, and vary on the host. Similar to Annotation,
    the host indicates who logged the event. This allows you to tell the
    difference between the client and server side of the same key. For example,
    the key "http.uri" might be different on the client and server side due to
    rewriting, like "/api/v1/myresource" vs "/myresource. Via the host field,
    you can see the different points of view, which often help in debugging.

    Attributes:
     - key
     - value
     - annotation_type
     - host: The host that recorded tag, which allows you to differentiate between
    multiple tags with the same key. There are two exceptions to this.

    When the key is CLIENT_ADDR or SERVER_ADDR, host indicates the source or
    destination of an RPC. This exception allows zipkin to display network
    context of uninstrumented services, or clients such as web browsers.
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'key', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'value', 'BINARY', None, ),  # 2
        (3, TType.I32, 'annotation_type', None, None, ),  # 3
        (4, TType.STRUCT, 'host', (Endpoint, Endpoint.thrift_spec), None, ),  # 4
    )

    def __init__(self, key=None, value=None, annotation_type=None, host=None,):
        self.key = key
        self.value = value
        self.annotation_type = annotation_type
        self.host = host

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.key = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.value = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.annotation_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.host = Endpoint()
                    self.host.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('BinaryAnnotation')
        if self.key is not None:
            oprot.writeFieldBegin('key', TType.STRING, 1)
            oprot.writeString(self.key.encode('utf-8') if sys.version_info[0] == 2 else self.key)
            oprot.writeFieldEnd()
        if self.value is not None:
            oprot.writeFieldBegin('value', TType.STRING, 2)
            oprot.writeBinary(self.value)
            oprot.writeFieldEnd()
        if self.annotation_type is not None:
            oprot.writeFieldBegin('annotation_type', TType.I32, 3)
            oprot.writeI32(self.annotation_type)
            oprot.writeFieldEnd()
        if self.host is not None:
            oprot.writeFieldBegin('host', TType.STRUCT, 4)
            self.host.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(L)})"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Span(object):
    """
    A trace is a series of spans (often RPC calls) which form a latency tree.

    The root span is where trace_id = id and parent_id = Nil. The root span is
    usually the longest interval in the trace, starting with a SERVER_RECV
    annotation and ending with a SERVER_SEND.

    Attributes:
     - trace_id
     - name: Span name in lowercase, rpc method for example

    Conventionally, when the span name isn't known, name = "unknown".
     - id
     - parent_id
     - annotations
     - binary_annotations
     - debug
     - timestamp: Microseconds from epoch of the creation of this span.

    This value should be set directly by instrumentation, using the most
    precise value possible. For example, gettimeofday or syncing nanoTime
    against a tick of currentTimeMillis.

    For compatibilty with instrumentation that precede this field, collectors
    or span stores can derive this via Annotation.timestamp.
    For example, SERVER_RECV.timestamp or CLIENT_SEND.timestamp.

    This field is optional for compatibility with old data: first-party span
    stores are expected to support this at time of introduction.
     - duration: Measurement of duration in microseconds, used to support queries.

    This value should be set directly, where possible. Doing so encourages
    precise measurement decoupled from problems of clocks, such as skew or NTP
    updates causing time to move backwards.

    For compatibilty with instrumentation that precede this field, collectors
    or span stores can derive this by subtracting Annotation.timestamp.
    For example, SERVER_SEND.timestamp - SERVER_RECV.timestamp.

    If this field is persisted as unset, zipkin will continue to work, except
    duration query support will be implementation-specific. Similarly, setting
    this field non-atomically is implementation-specific.

    This field is i64 vs i32 to support spans longer than 35 minutes.
     - trace_id_high: Optional unique 8-byte additional identifier for a trace. If non zero, this
    means the trace uses 128 bit traceIds instead of 64 bit.
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I64, 'trace_id', None, None, ),  # 1
        None,  # 2
        (3, TType.STRING, 'name', 'UTF8', None, ),  # 3
        (4, TType.I64, 'id', None, None, ),  # 4
        (5, TType.I64, 'parent_id', None, None, ),  # 5
        (6, TType.LIST, 'annotations', (TType.STRUCT, (Annotation, Annotation.thrift_spec), False), None, ),  # 6
        None,  # 7
        (8, TType.LIST, 'binary_annotations', (TType.STRUCT, (BinaryAnnotation, BinaryAnnotation.thrift_spec), False), None, ),  # 8
        (9, TType.BOOL, 'debug', None, False, ),  # 9
        (10, TType.I64, 'timestamp', None, None, ),  # 10
        (11, TType.I64, 'duration', None, None, ),  # 11
        (12, TType.I64, 'trace_id_high', None, None, ),  # 12
    )

    def __init__(self, trace_id=None, name=None, id=None, parent_id=None, annotations=None, binary_annotations=None, debug=thrift_spec[9][4], timestamp=None, duration=None, trace_id_high=None,):
        self.trace_id = trace_id
        self.name = name
        self.id = id
        self.parent_id = parent_id
        self.annotations = annotations
        self.binary_annotations = binary_annotations
        self.debug = debug
        self.timestamp = timestamp
        self.duration = duration
        self.trace_id_high = trace_id_high

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.trace_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.parent_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.annotations = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = Annotation()
                        _elem5.read(iprot)
                        self.annotations.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.LIST:
                    self.binary_annotations = []
                    (_etype9, _size6) = iprot.readListBegin()
                    for _i10 in range(_size6):
                        _elem11 = BinaryAnnotation()
                        _elem11.read(iprot)
                        self.binary_annotations.append(_elem11)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.BOOL:
                    self.debug = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I64:
                    self.timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I64:
                    self.duration = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I64:
                    self.trace_id_high = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Span')
        if self.trace_id is not None:
            oprot.writeFieldBegin('trace_id', TType.I64, 1)
            oprot.writeI64(self.trace_id)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 3)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.I64, 4)
            oprot.writeI64(self.id)
            oprot.writeFieldEnd()
        if self.parent_id is not None:
            oprot.writeFieldBegin('parent_id', TType.I64, 5)
            oprot.writeI64(self.parent_id)
            oprot.writeFieldEnd()
        if self.annotations is not None:
            oprot.writeFieldBegin('annotations', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.annotations))
            for iter12 in self.annotations:
                iter12.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.binary_annotations is not None:
            oprot.writeFieldBegin('binary_annotations', TType.LIST, 8)
            oprot.writeListBegin(TType.STRUCT, len(self.binary_annotations))
            for iter13 in self.binary_annotations:
                iter13.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.debug is not None:
            oprot.writeFieldBegin('debug', TType.BOOL, 9)
            oprot.writeBool(self.debug)
            oprot.writeFieldEnd()
        if self.timestamp is not None:
            oprot.writeFieldBegin('timestamp', TType.I64, 10)
            oprot.writeI64(self.timestamp)
            oprot.writeFieldEnd()
        if self.duration is not None:
            oprot.writeFieldBegin('duration', TType.I64, 11)
            oprot.writeI64(self.duration)
            oprot.writeFieldEnd()
        if self.trace_id_high is not None:
            oprot.writeFieldBegin('trace_id_high', TType.I64, 12)
            oprot.writeI64(self.trace_id_high)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(L)})"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Response(object):
    """
    Attributes:
     - ok
    """

    thrift_spec = (
        None,  # 0
        (1, TType.BOOL, 'ok', None, None, ),  # 1
    )

    def __init__(self, ok=None,):
        self.ok = ok

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1 and ftype == TType.BOOL:
                self.ok = iprot.readBool()
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Response')
        if self.ok is not None:
            oprot.writeFieldBegin('ok', TType.BOOL, 1)
            oprot.writeBool(self.ok)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.ok is None:
            raise TProtocolException(message='Required field ok is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(L)})"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
