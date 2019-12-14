# flixbus2
This repo contains the programming problem to allocate Best Fit VM in given  cluster configuration.

# Problem Statement-

You are given a list of virtual machines defined by the required number of CPUs, amount of RAM (in GBs) and network bandwidth (in MBpS). You can order any number of servers of a specific given size, where the size is always equal or bigger than the biggest virtual machine in the list. Your goal is to write a function which, given a list of VMs and the server characteristics, returns the number of servers needed to fit all the VMs. Make an attempt to create an algorithm which minimises the number of servers needed. As an extra step please provide an allocation map as a second output of the function.

 

Examples:

 

Example 1:

VMs:

- 1 CPU, 2 GB RAM, 50MBpS

- 2 CPU, 1 GB RAM, 50MBpS 

Server: 3 CPU, 3 GB RAM, 200 MBpS

Answer: 1 server, 1st server: machine 1, machine 2

 

Example 2:

VMs:

- 1 CPU, 2 GB RAM, 50MBpS

- 2 CPU, 2 GB RAM, 50MBpS 

- 2 CPU, 2 GB RAM, 100MBpS 

Server: 3 CPU, 3 GB RAM, 200 MBpS

Answer: 3 servers, 1st server: machine 1, 2nd server: machine 2, 3rd server: machine 3.

 

 

Example 3:

VMs:

- 1 CPU, 2 GB RAM, 50MBpS

- 2 CPU, 1 GB RAM, 50MBpS 

- 2 CPU, 2 GB RAM, 100MBpS 

Server: 3 CPU, 3 GB RAM, 200 MBpS

Answer: 2 servers, 1st server: machine 1, machine 2, 2nd server: machine 3.


# Note-
This is not the perfect solution or best fit. This is just a working solution for this problem.
Please directly execute the file & have a look at the solution. I want to improve this to return Best Fit cluster configution.
As of now this script is return machines in sequential manner until requirements are fulfilled.
Please share your suggestions to mikhil.nagarale@gmail.com
 

 

