import java.lang.Math;

class ClimbingStairs {
    public int climbStairs(int n) {
        double d = 1/(Math.sqrt(5)) * (Math.pow(((1 + (Math.sqrt(5)))/2), n + 1) - Math.pow((((1 - (Math.sqrt(5))))/2), n + 1));
        return (int) d;
    }
}