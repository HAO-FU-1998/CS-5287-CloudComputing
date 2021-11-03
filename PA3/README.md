# CS5287 Cloud Computing Programming Assignment #3
--

Tasks:
- added playbooks to install docker & kubernetes
- VM2 will act as the master as well as one of the worker nodes
- VM3 will be a worker node only

Manual Setup of Kubernetes Cluster:
-

Setup VM2
--
`git clone https://github.com/asgokhale/CloudComputingCourse`

Build Cluster
--
`sudo kubeadm init --node-name kubemaster --pod-network-cidr=10.244.0.0/16`

`mkdir -p $HOME/.kube`

`sudo cp -i  /etc/kubernetes/admin.conf $HOME/.kube/config`

`sudo chown $(id -u):$(id -g) $HOME/.kube/config`

`kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml`

Join VM3 worker

`sudo kubeadm join ...` - match string from cluster init. Add `--node-name kubeworker2` to the end
kubeadm join 172.31.26.94:6443 --token zopelv.6mt3iodhqynvya2q --discovery-token-ca-cert-hash sha256:ce7eb1effe9d72102a27b634db767368120840dfeab1a356094abae755da888d --node-name kubeworker2

Back to VM2...

`sudo apt-get install jq`

`kubectl get nodes -o json | jq '.items[].spec.taints'`

`kubectl taint nodes kubemaster node-role.kubernetes.io/master:NoSchedule-`

Deployment Example
--
cd into the Deployments folder
`kubectl apply -f nginx-deployment.yaml`

`kubectl --record deployment.v1.apps/nginx-deployment set image deployment.v1.apps/nginx-deployment nginx=nginx:stable`

`kubectl expose deployment nginx-deployment --type=LoadBalancer --name=my-nginx`

`kubectl delete service my-nginx`

`kubectl delete deployment nginx-deployment`

`kubectl get pods -l app=nginx`

Jobs Example
--
cd into the Job folder
`sudo docker build -f ./dockerfile -t my_matinv .`

`sudo docker run -d -p 5000:5000 --restart=always --name registry registry:2`

`sudo docker tag my_matinv:latest {public_ip}:5000/my_matinv`

`sudo docker push {public_ip}:5000/my_matinv`
