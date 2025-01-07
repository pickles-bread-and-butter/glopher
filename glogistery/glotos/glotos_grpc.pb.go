// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.5.1
// - protoc             v3.12.4
// source: glotos.proto

package protos

import (
	context "context"
	empty "github.com/golang/protobuf/ptypes/empty"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.64.0 or later.
const _ = grpc.SupportPackageIsVersion9

const (
	Registry_GetPlugin_FullMethodName      = "/Registry/GetPlugin"
	Registry_RegisterPlugin_FullMethodName = "/Registry/RegisterPlugin"
	Registry_ListPlugins_FullMethodName    = "/Registry/ListPlugins"
)

// RegistryClient is the client API for Registry service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type RegistryClient interface {
	GetPlugin(ctx context.Context, in *PluginGetRequest, opts ...grpc.CallOption) (*PluginGetResponse, error)
	RegisterPlugin(ctx context.Context, in *PluginRegisterRequest, opts ...grpc.CallOption) (*PluginRegisterResponse, error)
	ListPlugins(ctx context.Context, in *empty.Empty, opts ...grpc.CallOption) (*PluginListResponse, error)
}

type registryClient struct {
	cc grpc.ClientConnInterface
}

func NewRegistryClient(cc grpc.ClientConnInterface) RegistryClient {
	return &registryClient{cc}
}

func (c *registryClient) GetPlugin(ctx context.Context, in *PluginGetRequest, opts ...grpc.CallOption) (*PluginGetResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(PluginGetResponse)
	err := c.cc.Invoke(ctx, Registry_GetPlugin_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *registryClient) RegisterPlugin(ctx context.Context, in *PluginRegisterRequest, opts ...grpc.CallOption) (*PluginRegisterResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(PluginRegisterResponse)
	err := c.cc.Invoke(ctx, Registry_RegisterPlugin_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *registryClient) ListPlugins(ctx context.Context, in *empty.Empty, opts ...grpc.CallOption) (*PluginListResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(PluginListResponse)
	err := c.cc.Invoke(ctx, Registry_ListPlugins_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// RegistryServer is the server API for Registry service.
// All implementations must embed UnimplementedRegistryServer
// for forward compatibility.
type RegistryServer interface {
	GetPlugin(context.Context, *PluginGetRequest) (*PluginGetResponse, error)
	RegisterPlugin(context.Context, *PluginRegisterRequest) (*PluginRegisterResponse, error)
	ListPlugins(context.Context, *empty.Empty) (*PluginListResponse, error)
	mustEmbedUnimplementedRegistryServer()
}

// UnimplementedRegistryServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedRegistryServer struct{}

func (UnimplementedRegistryServer) GetPlugin(context.Context, *PluginGetRequest) (*PluginGetResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetPlugin not implemented")
}
func (UnimplementedRegistryServer) RegisterPlugin(context.Context, *PluginRegisterRequest) (*PluginRegisterResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RegisterPlugin not implemented")
}
func (UnimplementedRegistryServer) ListPlugins(context.Context, *empty.Empty) (*PluginListResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ListPlugins not implemented")
}
func (UnimplementedRegistryServer) mustEmbedUnimplementedRegistryServer() {}
func (UnimplementedRegistryServer) testEmbeddedByValue()                  {}

// UnsafeRegistryServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to RegistryServer will
// result in compilation errors.
type UnsafeRegistryServer interface {
	mustEmbedUnimplementedRegistryServer()
}

func RegisterRegistryServer(s grpc.ServiceRegistrar, srv RegistryServer) {
	// If the following call pancis, it indicates UnimplementedRegistryServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&Registry_ServiceDesc, srv)
}

func _Registry_GetPlugin_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PluginGetRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(RegistryServer).GetPlugin(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Registry_GetPlugin_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(RegistryServer).GetPlugin(ctx, req.(*PluginGetRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Registry_RegisterPlugin_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PluginRegisterRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(RegistryServer).RegisterPlugin(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Registry_RegisterPlugin_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(RegistryServer).RegisterPlugin(ctx, req.(*PluginRegisterRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Registry_ListPlugins_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(empty.Empty)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(RegistryServer).ListPlugins(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Registry_ListPlugins_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(RegistryServer).ListPlugins(ctx, req.(*empty.Empty))
	}
	return interceptor(ctx, in, info, handler)
}

// Registry_ServiceDesc is the grpc.ServiceDesc for Registry service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Registry_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "Registry",
	HandlerType: (*RegistryServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetPlugin",
			Handler:    _Registry_GetPlugin_Handler,
		},
		{
			MethodName: "RegisterPlugin",
			Handler:    _Registry_RegisterPlugin_Handler,
		},
		{
			MethodName: "ListPlugins",
			Handler:    _Registry_ListPlugins_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "glotos.proto",
}

const (
	Plugin_UnaryCallPlugin_FullMethodName = "/Plugin/UnaryCallPlugin"
)

// PluginClient is the client API for Plugin service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type PluginClient interface {
	UnaryCallPlugin(ctx context.Context, in *PluginUnaryRequest, opts ...grpc.CallOption) (*PluginUnaryResponse, error)
}

type pluginClient struct {
	cc grpc.ClientConnInterface
}

func NewPluginClient(cc grpc.ClientConnInterface) PluginClient {
	return &pluginClient{cc}
}

func (c *pluginClient) UnaryCallPlugin(ctx context.Context, in *PluginUnaryRequest, opts ...grpc.CallOption) (*PluginUnaryResponse, error) {
	cOpts := append([]grpc.CallOption{grpc.StaticMethod()}, opts...)
	out := new(PluginUnaryResponse)
	err := c.cc.Invoke(ctx, Plugin_UnaryCallPlugin_FullMethodName, in, out, cOpts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// PluginServer is the server API for Plugin service.
// All implementations must embed UnimplementedPluginServer
// for forward compatibility.
type PluginServer interface {
	UnaryCallPlugin(context.Context, *PluginUnaryRequest) (*PluginUnaryResponse, error)
	mustEmbedUnimplementedPluginServer()
}

// UnimplementedPluginServer must be embedded to have
// forward compatible implementations.
//
// NOTE: this should be embedded by value instead of pointer to avoid a nil
// pointer dereference when methods are called.
type UnimplementedPluginServer struct{}

func (UnimplementedPluginServer) UnaryCallPlugin(context.Context, *PluginUnaryRequest) (*PluginUnaryResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UnaryCallPlugin not implemented")
}
func (UnimplementedPluginServer) mustEmbedUnimplementedPluginServer() {}
func (UnimplementedPluginServer) testEmbeddedByValue()                {}

// UnsafePluginServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to PluginServer will
// result in compilation errors.
type UnsafePluginServer interface {
	mustEmbedUnimplementedPluginServer()
}

func RegisterPluginServer(s grpc.ServiceRegistrar, srv PluginServer) {
	// If the following call pancis, it indicates UnimplementedPluginServer was
	// embedded by pointer and is nil.  This will cause panics if an
	// unimplemented method is ever invoked, so we test this at initialization
	// time to prevent it from happening at runtime later due to I/O.
	if t, ok := srv.(interface{ testEmbeddedByValue() }); ok {
		t.testEmbeddedByValue()
	}
	s.RegisterService(&Plugin_ServiceDesc, srv)
}

func _Plugin_UnaryCallPlugin_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(PluginUnaryRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(PluginServer).UnaryCallPlugin(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: Plugin_UnaryCallPlugin_FullMethodName,
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(PluginServer).UnaryCallPlugin(ctx, req.(*PluginUnaryRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Plugin_ServiceDesc is the grpc.ServiceDesc for Plugin service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Plugin_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "Plugin",
	HandlerType: (*PluginServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "UnaryCallPlugin",
			Handler:    _Plugin_UnaryCallPlugin_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "glotos.proto",
}
