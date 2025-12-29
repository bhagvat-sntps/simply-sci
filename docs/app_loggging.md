



## log customization
below flow is applied when needs to attach correlation-id / trace_id to each http request


```
Incoming HTTP request
        │
        ▼
Middleware
  ├─ Read x-correlation-id OR generate UUID
  ├─ Store values in contextvars
        │
        ▼
Business code (routes, services, db)
  ├─ logger.info(...)
  └─ Logging Filter injects context
        │
        ▼
JSON Formatter
        │
        ▼
STDOUT (K8s → Loki / ELK)
```