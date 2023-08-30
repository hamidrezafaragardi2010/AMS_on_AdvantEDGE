# AMS on AdvantEDGE
AdvantEDGE is a Mobile Edge Emulation Platform (MEEP) that runs on Docker & Kubernetes.

It provides an emulation environment, enabling experimentation with Edge Computing Technologies, Applications, and Services. The platform facilitates exploring edge / fog deployment models and their impact on applications and services in short and agile iterations.

We implemented a heartbeat script that update the location of UE every second. It showcases the Application Mobility Service (AMS) on between edge hosts.

# Installation Guide
1. Install docker on the machine
2. Install Kubernetes
3. Install AdvantEDGE on the top K8s
4. Import the yaml scenario file
5. Switch the scenario into map
6. Create a new sandbox
7. Deploy the scenario
8. Run ams.py file
9. Set an approperiate speed for the UE
10. See the UE movement and its zone changing due to the AMS
