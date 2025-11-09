resource "aws_s3_bucket" "myS3bucket" {
	bucket="s3bucket-created-14092025"
	tags = {
		name="myS3Bucket"
}
}
