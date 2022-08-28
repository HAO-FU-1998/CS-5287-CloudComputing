# Provisioning Automation using DevOps-based Deployment and Configuration of Simple Data Analytics Pipeline in Cloud Virtual Machines

You will repeat what we did in Assignment #1 but this time everything will be driven through a combination of Vagrant and Ansible. So, you will write the appropriate Vagrantfile, which will spawn a local VM on your laptop (say VM1.1 but VM1.2 can still be the manually created). VM1.1 in turn will automatically run a variety of Ansible playbooks from a master playbook (all of which you will design) to spawn the VM2 and VM3 in Chameleon cloud. The process should also deploy the application code and start the applications. Our aim is to achieve 100% automation. See how much you are able to.

We will use the clouds.yaml file to store our Openstack CLI credentials. Those working on AWS will find an equivalent approach to do so. Reuse your modified producer and consumer code for this assignment.


# Why these technologies?
-	Vagrant and Ansible are representative DevOps technologies and are widely used. Several other technologies exist like Chef, Puppet, Terraform, AWS CloudFormation etc but it will be hard to learn all these technologies and hence we choose some representative sample among them.
# Data collection
As you are doing this assignment, although I have provided scaffolding code and slides to help you get started, there will still be enough learning curve, and trial/error. Please keep track of the effort in the learning curve and trial/error to get the scripts right, but then check how seamless is it to move between clouds and how much automation did you achieve. 
