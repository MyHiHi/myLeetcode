object Hello{
  trait Handler{
    def handle(data:String){
      println("handle: ",data)
    }
  }
  trait Start extends Handler{
    override def handle(data1:String)={
      println(s"solving data ${data1}......")
      super.handle(data1)
    }
  }
  trait DataVaildHandler extends Handler{
    override def handle(data:String)={
      println("vaildData:",data);
      super.handle(data)
    }
  }
  trait SignnatureVaildHandler extends Handler{
    override def handle(data:String)={
      println("signnatureVaild Data: ",data);
      super.handle(data)
    }
  }
  class Person(val name:String) extends SignnatureVaildHandler with DataVaildHandler with Start{
    def sayHello={
      println("Hello "+name);
      handle(name)
    }
  }
  def main(args: Array[String]): Unit = {
    val p=new Person("Leo");
    p.sayHello
  }
}