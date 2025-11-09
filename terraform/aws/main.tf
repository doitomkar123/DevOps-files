resource "aws_key_pair" "myKeyPair" {
	key_name="myEC2Key"
	public_key=file("~/.ssh/my_key.pub")
}

resource "aws_instance" "myInstance" {
	ami = "ami-0360c520857e3138f"
	instance_type = "t2.micro"
	key_name=aws_key_pair.myKeyPair.key_name
	tags = {
		name="instance by TF"	
}
}
