def get_config(current_capacity,required_capacity):
    if current_capacity<=required_capacity:
        return current_capacity
    else:
        return required_capacity    

def printRequest(cluster_vm_config,server_requirement,alloted_servers):
    print("Cluster Configuration :" +str(cluster_vm_config).replace('C','CPU').replace('S','Speed').replace('R','RAM'))
    print("Server Requirement :"+ str(server_requirement).replace('C','CPU').replace('S','Speed').replace('R','RAM'))
    print("Alloted Servers :-")
    server_index=1    
    for server in alloted_servers:
        print('Server {} machine {}'.format(server_index,server))    
        server_index += 1
    print()


def get_cluster(cluster_vm_config,server_requirement):
    alloted_servers = []
    result=''
    required_config = server_requirement.copy()
    while any([required_config['C']>0,required_config['R']>0,required_config['S']>0]):
        machine_list = []
        machine_index = 1
        for machine in cluster_vm_config: 
            if any([required_config['C']>0,required_config['R']>0,required_config['S']>0]):
                for k,v in machine.items():
                    required_config[k] -= get_config(machine[k],required_config[k])
                machine_list.append(machine_index)    
                machine_index += 1    
        alloted_servers.append(machine_list)
    printRequest(cluster_vm_config,server_requirement,alloted_servers)


if __name__ == "__main__":
    get_cluster([{'C':1,'R':2,'S':50},{'C':2,'R':1,'S':50}],{'C':3,'R':3,'S':200})   
    get_cluster([{'C':1,'R':2,'S':50},{'C':2,'R':2,'S':50},{'C':2,'R':2,'S':100}],{'C':3,'R':3,'S':200})    
    get_cluster([{'C':1,'R':2,'S':50},{'C':2,'R':1,'S':50},{'C':2,'R':2,'S':100}],{'C':6,'R':3,'S':200})     

