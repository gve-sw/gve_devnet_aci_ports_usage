import requests, json, os
from flask import Flask, render_template
from dotenv import load_dotenv
load_dotenv()

base=os.environ["base"]
requests.packages.urllib3.disable_warnings()
app = Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def main():

    inter=get_nodes_interfaces()
    headers=['Pod','Node','Int',"Int in Use","Free Int","Reserved Int"]

    return render_template('index.html', header=headers, inter=inter)



def get_token():
    user=os.environ["user"]
    password=os.environ["password"]
    url = f"{base}/aaaLogin.json"
    payload = {
            "aaaUser": {
                "attributes": {
                    "name": user,
                    "pwd": password
                }
            }
        }
    headers = {'Content-Type': 'text/plain'}
    response = requests.request("POST", url, headers=headers, json=payload, verify=False)
    if response.status_code == 200:
        token = response.json()['imdata'][0]['aaaLogin']['attributes']['token']
        return token


def get_fabric_nodes():
    token = get_token()
    url = f"{base}/node/class/fabricNode.json?query-target-filter=ne(fabricNode.role, %22controller%22)"
    headers = {
        "Cookie": f"APIC-Cookie={token}",
    }
    response = requests.get(url, headers=headers, verify=False).json()
   
    dn=[]
    for r in response["imdata"]:
        d=[]
        d.append(r["fabricNode"]["attributes"]["dn"])
        d.append(r["fabricNode"]["attributes"]["name"])
        dn.append(d)
    return dn

def get_nodes_interfaces():
    token = get_token()
    int_all=[]
    dn=get_fabric_nodes()
    for d in dn:
            node_info={}
            url= f'{base}/node/class/{d[0]}/l1PhysIf.json?rsp-subtree=children&rsp-subtree-class=ethpmPhysIf'
            headers = {
                "Cookie": f"APIC-Cookie={token}",
            }

            response = requests.get(url, headers=headers, verify=False).json()
            
            ports=response["totalCount"]
            ports_in_use=0
            free_ports=0
            reserved_ports=0
            for r in response["imdata"]:
                if r["l1PhysIf"]["attributes"]["descr"] == "Reserved":
                    reserved_ports+=1
                else:
                    for rr in r["l1PhysIf"]["children"]:
                        if rr["ethpmPhysIf"]["attributes"]["operSt"]=="down":
                            free_ports+=1
                        else:
                            ports_in_use+=1

                    
            node=d[0].split("/")
            node_info["pod"]=node[1]
            node_info["name"]=node[2]
            node_info["ports"]=ports
            node_info["ports_in_use"]=ports_in_use
            node_info["free_ports"]=free_ports
            node_info["reserved"]=reserved_ports
            node_info["node_name"]=d[1]
            int_all.append(node_info)
      
    return int_all
            


if __name__ == "__main__":
    app.run(port=5010,debug=True)