
fun main() {
    println("Hello, world!")
    println(5)
    println("Sum is ${sum(5,5)}")
    vars(6)
    val ret = conditional(2,3)
    println("$ret is greater")
    println("Expression find solution: ${greaterexp(2,4)}")
    
}
fun println(a: Int) {
    println("hey its, "+a)
}
fun sum(a:Int, b:Int) = a + b
fun vars(a:Int) {
    //val is like const u cant change it
    //var can be changed
    var pi = 3.14
    println("Before changing:$pi")
    pi = 3.143
    println("After changing:$pi")
    val st = "gayatri hungund"
    val exp = "the number here is $a but lets replace something $st is now ${st.replace("gayatri","gayu")}"
    println(exp)
}
fun conditional(a:Int, b:Int): Int {
    if (a>b){
        return a
    } else {
        return b
    }
}
fun greaterexp(a:Int,b:Int) = if (a>b) a else b
