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
public class ball {
    private  double x,y,r; //x,y is center of ball and r is radius
    private  double xDelta,yDelta;
    public ball(double x, double y, double r,double speed , double direction)
    {
        this.x=x;
        this.y=y;
        this.r=r;
        this.xDelta=(speed)*(Math.cos(Math.PI*direction/180));
        this.yDelta=-(speed)*(Math.sin(Math.PI*direction/180));
     }
    
    public void setX(double x)
    {
        this.x=x;
    }
    public double getX()
    {
        return x;
    }
    public void setY(double y)
    {
        this.y=y;
    }
    public double getY()
    {
        return y;
    }
    public void setRadius(double r)
    {
        this.r=r;
    }
    public double getRadius()
    {
        return r;
    }
    public void setXDelta(double speed, double direction)
    {
        this.xDelta=(speed)*(Math.cos(Math.PI*direction/180));
    }
    public double getXDelta()
    {
        return xDelta;
    }
    public void setYDelta(double speed,double direction)
    {
        this.yDelta=-(speed)*(Math.sin(Math.PI*direction/180));
    }
    public double getYDelta()
    {
        return yDelta;
    }
    public void move()
    {
        x=x+xDelta;
        y=y+yDelta;
    }
    public void reflectHorizontal()
    {
        xDelta=-xDelta;
    }
    public void reflectVertical()
    {
        yDelta=-yDelta;
    }
    @Override
    public String  toString()
    {
        return "Ball at (" + x + ", "+ y + ") of velocity (" + xDelta +"," + yDelta + ")";
    }

   
    
        
    
     
            
    
    
    
    
}
