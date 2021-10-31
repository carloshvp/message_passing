import time
from concurrent import futures

import grpc
import order_pb2
import order_pb2_grpc


class OrderServicer(order_pb2_grpc.OrderService):
    def Create(self, request, context):

        request_value = {
            "id" : request.id,
            "created_by" : request.created_by,
            "status" : request.status,
            "created_at" : request.created_at,
            "equipment" : request.equipment
        }
        print(request_value)

        return order_pb2.OrderMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
order_pb2_grpc.add_OrderServiceServicer_to_server(OrderServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
