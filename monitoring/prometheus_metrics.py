from prometheus_client import start_http_server, Summary

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

def record_metrics(length):
    REQUEST_TIME.observe(length)

start_http_server(8001)