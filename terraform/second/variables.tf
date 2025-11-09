variable "filename" {
	default="/tmp/variable_text.txt"
	type=string
	description="variables text file"
}

variable "content" {
	default="this is from terraform"
}

variable "myStringLen" {
	default=10
}

variable "listVar" {
	default=["/tmp/secondFile.txt", "This is second file"]
	type=list
}
