resource "local_file" "testFile" {
  filename="/tmp/taintCheck.txt"
  content="taint test"
}
