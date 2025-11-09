variable "myVariable" {
  type = string
}

output "myOutput" {
  value = var.myVariable
}

resource "local_file" "myFile" {
  filename = "/tmp/envFileTF.txt"
  content  = "My Variable Value -> ${var.myVariable}"
}
