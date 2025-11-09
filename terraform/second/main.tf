resource "local_file" "myFile" {
	filename=var.filename
	content=var.content
}

resource "local_file" "secondFile" {
	filename=var.listVar[0]
	content="second file randomString ${random_string.myString.id}"
}

resource "random_string" "myString" {
	length=var.myStringLen
}

output "stringOutput" {
	value="${random_string.myString.id}"
}
