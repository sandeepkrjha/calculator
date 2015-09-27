/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication2;

/**
 *
 * @author san_jha
 */
public class Container {

    private int x1, x2, y1, y2;//(x1,y1)is top left corner of rectangular box and (x2,y2)is bottom-right

    public Container(int x, int y, int width, int height) {
        this.x1 = x;
        this.y1 = y;
        this.x2 = x1 + width - 1;
        this.y2 = y2 + height - 1;
    }

    public void setX1(int x) {
        this.x1 = x;

    }

    public int getX1() {
        return x1;
    }

    public void setY1(int y) {
        this.y1 = y;
    }

    public int getY1() {
        return y1;
    }

    public void setX2(int x) {
        this.x2 = x;
    }

    public int getX2() {
        return x2;
    }

    public void setY2(int y) {
        this.y2 = y;

    }

    public int getY2() {
        return y2;
    }

    @Override
    public String toString() {
        return "container at (" + x1 + "," + y1 + ") to (" + x2 + "," + y2 + ")";
    }

    /**
     *
     * @param ball
     * @return
     */
    public boolean collideWith(ball ball) {
        if (ball.getX() - ball.getRadius() <= this.x1 || ball.getX() - ball.getRadius() >= this.x2) {
            ball.reflectHorizontal();
            return true;
        }
        if (ball.getY() - ball.getRadius() <= this.y1 || ball.getY() - ball.getRadius() >= this.y2) {
            ball.reflectVertical();
            return true;
        }
        return false;

    }

}
