resource "aws_db_instance" "default" {
  allocated_storage    = 20
  db_name              = "api_db"
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t2.micro"
  username             = "python_user"
  password             = var.password
  parameter_group_name = "default.mysql5.7"
  skip_final_snapshot  = true
}