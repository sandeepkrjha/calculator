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
public class testBallroom {
    public static void main(String [] args)
    {
        ball ball= new ball(50,50,5,10,30);
        Container box = new Container(0,0,100,100);
        for(int step=0;step<100;++step)
        {
            ball.move();
            box.collideWith(ball);
            System.out.println(ball);
        }
    }
        
    
}
