# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import todo_pb2 as todo__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in todo_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class todoServiceStub(object):
    """Service 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Addtodo = channel.unary_unary(
                '/todoService/Addtodo',
                request_serializer=todo__pb2.todo.SerializeToString,
                response_deserializer=todo__pb2.todo.FromString,
                _registered_method=True)
        self.GetAll = channel.unary_unary(
                '/todoService/GetAll',
                request_serializer=todo__pb2.Empty.SerializeToString,
                response_deserializer=todo__pb2.todoList.FromString,
                _registered_method=True)
        self.Gettodo = channel.unary_unary(
                '/todoService/Gettodo',
                request_serializer=todo__pb2.todoTitle.SerializeToString,
                response_deserializer=todo__pb2.todo.FromString,
                _registered_method=True)
        self.Updatetodo = channel.unary_unary(
                '/todoService/Updatetodo',
                request_serializer=todo__pb2.todo.SerializeToString,
                response_deserializer=todo__pb2.todo.FromString,
                _registered_method=True)
        self.Deletetodo = channel.unary_unary(
                '/todoService/Deletetodo',
                request_serializer=todo__pb2.todoId.SerializeToString,
                response_deserializer=todo__pb2.Empty.FromString,
                _registered_method=True)


class todoServiceServicer(object):
    """Service 
    """

    def Addtodo(self, request, context):
        """Create
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAll(self, request, context):
        """Read 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Gettodo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Updatetodo(self, request, context):
        """Update
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deletetodo(self, request, context):
        """Delete
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_todoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Addtodo': grpc.unary_unary_rpc_method_handler(
                    servicer.Addtodo,
                    request_deserializer=todo__pb2.todo.FromString,
                    response_serializer=todo__pb2.todo.SerializeToString,
            ),
            'GetAll': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=todo__pb2.Empty.FromString,
                    response_serializer=todo__pb2.todoList.SerializeToString,
            ),
            'Gettodo': grpc.unary_unary_rpc_method_handler(
                    servicer.Gettodo,
                    request_deserializer=todo__pb2.todoTitle.FromString,
                    response_serializer=todo__pb2.todo.SerializeToString,
            ),
            'Updatetodo': grpc.unary_unary_rpc_method_handler(
                    servicer.Updatetodo,
                    request_deserializer=todo__pb2.todo.FromString,
                    response_serializer=todo__pb2.todo.SerializeToString,
            ),
            'Deletetodo': grpc.unary_unary_rpc_method_handler(
                    servicer.Deletetodo,
                    request_deserializer=todo__pb2.todoId.FromString,
                    response_serializer=todo__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class todoService(object):
    """Service 
    """

    @staticmethod
    def Addtodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todoService/Addtodo',
            todo__pb2.todo.SerializeToString,
            todo__pb2.todo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todoService/GetAll',
            todo__pb2.Empty.SerializeToString,
            todo__pb2.todoList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Gettodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todoService/Gettodo',
            todo__pb2.todoTitle.SerializeToString,
            todo__pb2.todo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Updatetodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todoService/Updatetodo',
            todo__pb2.todo.SerializeToString,
            todo__pb2.todo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Deletetodo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/todoService/Deletetodo',
            todo__pb2.todoId.SerializeToString,
            todo__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
