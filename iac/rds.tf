resource "aws_db_instance" "default" {
  allocated_storage    = 20
  db_name              = "my-test-db"
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t2.micro"
  username             = "db-test"
  password             = "W1q2e3%r"
  parameter_group_name = "default.mysql5.7"
  skip_final_snapshot  = true
}