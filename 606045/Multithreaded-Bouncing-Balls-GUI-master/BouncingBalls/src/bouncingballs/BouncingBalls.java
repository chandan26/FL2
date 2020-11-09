/* 
 *
 * BouncingBalls.java is comprises of two classes: BouncingBalls, which hosts
 * main(), creates the GUI, creates a BallPanel object, and enters into an 
 * infinite loop for repainting moving ball objects; and, BallPanel, which 
 * uses a MouseEvent listener to create a ball object (method createBall()) on 
 * each mouse click, store it in a Linked List, and overrides paintComponent to
 * paint the balls and a signature block. Method moveBall() is called from
 * main() for the purpose of repainting BallPanel. Each Ball object is executed
 * via ExecutorService in its own thread.
 */

package bouncingballs;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.concurrent.*;
import java.util.Random;

public class BouncingBalls
{
    public static void main(String[] args)
    {
        BallPanel b = new BallPanel(); // Create BallPanel - JPanel Object
        JFrame f = new JFrame("Multi Threading");
        f.setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE );
        f.add( b );
        f.setBackground(Color.BLACK);
        f.pack();
        f.setVisible(true);
        f.setResizable(false);
        while(true)
        {
            f.repaint(); // Repaint JFrame's black background
            b.moveBall(); // Move each Ball object
            try
            {
                Thread.sleep(10);
            }
            catch(Exception event){}
        }        
    } // End main
        
} // End BouncingBalls class

class BallPanel extends JPanel
{
    private ArrayList<Ball> balls;
    private final Random colorGenerator = new Random();
    private ExecutorService threadExecutor;
    private Color ballColor;
    private Student_Sig_Block sig;
    private Integer numBalls = 0;

    // constructor
    public BallPanel()
    {
        sig = new Student_Sig_Block(52);
        balls = new ArrayList();
        threadExecutor = Executors.newCachedThreadPool();        
        addMouseListener(
            new MouseAdapter()
            {
                @Override
                public void mouseClicked( MouseEvent e )
                {
                    createBall( e.getX(), e.getY() );
                    numBalls = balls.size();
                } // end mouseClicked
            } // end MouseAdapter()
        ); // End anonymous inner class
    } // End BouncingBalls constructor

    // Creates a BouncingBall, and executes it in a thread, for each mouse click
    public void createBall(double x, double y)
    {
        // Randomly generate a ball color
        ballColor = new Color( colorGenerator.nextInt(255),colorGenerator.nextInt(255),colorGenerator.nextInt(255) );
        // Add new ball object to a LinkedList
        balls.add( new Ball( ballColor, x, y) );
        // Executes new thread of created ball object
        threadExecutor.execute( balls.get(balls.size() - 1) );
    } // end createBall() method
    
    // Called from loop in main() to continuously repaint BallPanel()
    public void moveBall()
    {
        repaint();
    } // end moveBall() method
    
    // Sets the default JPanel size when pack() is called
    @Override
    public Dimension getPreferredSize()
    {
        return new Dimension(640, 480);
    } // End Overloaded JPanel Dimension
    
    // Overridden paintComponent() method to display balls and signature block
    @Override
    public void paintComponent(Graphics g)
    {
        super.paintComponents(g);
        Graphics2D g2d = (Graphics2D) g;
        for( Ball ball : balls)
        {
            g2d.setPaint( ball.getBallColor() );
            g2d.fillOval((int) ball.getBallCoords().getX(), (int) ball.getBallCoords().getY(), (int) ball.getBallDimension().getWidth(), (int) ball.getBallDimension().getHeight() );
        }
        
      // Display signature block information
      g.setColor(Color.WHITE);
      g.fillRect(50, 20, 365, 80);
      
      g.setColor(Color.BLACK);
      g.setFont(new Font("Courier New", Font.PLAIN, 12));      
      g.drawString(sig.border, 50, 30);
      g.drawString(sig.getName(), 65, 50);
      g.drawString("Balls created:  " + numBalls.toString(), 275, 50);
      g.drawString("Active Threads: " + Thread.activeCount(), 275, 65);
      g.drawString(sig.getEmail(), 65, 65);
      g.drawString(sig.getCourse(), 65, 80);      
      g.drawString(sig.border, 50, 100);        
   
    } // End Overloaded paintCompenent()
} // end MyPanel class