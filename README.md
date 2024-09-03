# Indoor-Parking-Assistance-System-using-Object-Detection
This repository contains the necessary content for an **Indoor Parking Assistance System** that uses **object detection** to identify empty parking spaces and provides **real-time navigation** to guide drivers to them. The system aims to improve parking efficiency and reduce the time spent searching for available spots in indoor environments.

```mermaid
graph TD
    A[User's Smartphone] -->|1. Scan Single QR Code| B[Web Application]
    B <-->|2. API Requests/Responses| C[Backend Server]
    C <-->|3. Data Storage/Retrieval| D[Database]
    C <-->|4. Position Updates| E[Indoor Positioning System]
    C <-->|5. Space Status Updates| F[Parking Space Management]
    G[CCTV Cameras] -->|6. Video Feed| H[Computer Vision System]
    H -->|7. Occupancy Data| F
    I[3D Map Rendering Engine] <-->|8. Map Data| B
    J[Navigation Algorithm] <-->|9. Path Calculations| B
    K[Single QR Code] -->|10. Display| L[Main Entry Point]
    L -->|11. Scan| A
    M[Admin Dashboard] <-->|12. Management Interface| C
    N[IoT Devices] -->|13. Sensor Data| E
    O[Payment Gateway] <-->|14. Process Payments| C
    P[Data Analytics Engine] <-->|15. Analyze Data| C
    Q[Push Notification Service] <-->|16. Send Alerts| C
    R[User Authentication Service] <-->|17. Verify User| C
    S[Space Allocation Algorithm] <-->|18. Assign Space| C

    subgraph "Mobile Experience"
        A
    end

    subgraph "Frontend"
        B
        I
        J
    end

    subgraph "Backend Infrastructure"
        C
        D
        E
        F
        H
        M
        O
        P
        Q
        R
        S
    end

    subgraph "Physical Infrastructure"
        G
        K
        L
        N
    end
```
