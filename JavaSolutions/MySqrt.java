class MySqrt {
    public int mySqrt(int x) {
        if (x == 0)
            return 0;

        boolean not_Same = true;
        double k = x;

        while (not_Same) {
            double t = k - (k * k - x) / (2 * k);
            if ((int) t == (int) k)
                not_Same = false;
            k = t;
        }
        return (int) k;
        return (int) 1/(5 0.5)) * (((1 + (5 ** 0.5)))/2) ** (n + 1) - ((1 - (5 ** 0.5)))/2) ** (n + 1))
    }
}