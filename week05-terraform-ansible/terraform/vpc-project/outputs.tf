output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.cloud_vpc.id
}

output "public_subnet_id" {
  description = "ID of the public subnet"
  value       = aws_subnet.public_subnet.id
}

output "web_server_public_ip" {
  description = "Public IP address of the web server"
  value       = aws_instance.web_server.public_ip
}

output "web_server_url" {
  description = "URL of the web server"
  value       = "http://${aws_instance.web_server.public_ip}"
}