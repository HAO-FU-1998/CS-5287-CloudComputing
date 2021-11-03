How to run:
===========

- Clone this repository to your local machine
- Ensure your keys match the Vagrantfile for name and location
- Pull fresh AWS credentials and update your ~/.aws/credentials file
- From this directory:
`vagrant up`

You should end up with an active VirtualBox instance with a running producer outputting to AWS VM2.

You can verify the producer output by doing a `vagrant ssh` and then `tail -f output.txt`
