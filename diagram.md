```mermaid
flowchart LR
    A[Customer System / Client App] -->|1. POST /api/login (username, password)| B[API Gateway (KingslakeBlue)]
    
    B --> C[Authentication Service]
    C -->|Validate Credentials| D[(User Database)]
    
    C -->|2. Generate JWT Token| B
    B -->|Return Token| A

    A -->|3. API Request + Bearer Token| B
    
    B -->|Validate Token| E[Auth Middleware / Token Validator]
    
    E -->|Valid| F[Line Balancing Service]
    F --> G[(Employee Database)]
    
    F -->|4. Employee Data Response| B
    B -->|Response| A

    E -->|Invalid Token| H[401 Unauthorized]
```