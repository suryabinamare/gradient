import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to solve quadratic equations
def partial_derivative(f,x):
    fx = sp.diff(f, x)
    return fx


def direct_derivative(f, I, T):
    V = np.array(T)-np.array(I)
    L = np.linalg.norm(V)
    U = V/L
    fx = sp.diff(f,x)
    fy = sp.diff(f,y)
    a = fx.subs({x:I[0], y:I[1]})
    b = fy.subs({x:I[0], y:I[1]})
    G = np.array([a,b])
    DD = np.dot(U,G)
    return DD, G, U
def funct_eval(f, I):
    value = f.subs({x:I[0], y:I[1]})
    return value



def graph_direction(a,b,c,d):
    radius = 1

    # Create a figure and an axes
    fig, ax = plt.subplots(figsize = (3,3))

    # Create a circle
    # circle = patches.Circle((a,b), radius, edgecolor='blue', facecolor='none')

    # Add the circle to the plot
    # ax.add_patch(circle)
    ax.plot(a,b, 'ro')
    #Add vector
    ax.quiver(a,b, c,d,angles = 'xy', scale_units = 'xy', scale = 1)

    # Add text near the point
    ax.text(a,b, f'({a},{b})', fontsize=12, ha='left', va='bottom')


    # Set the aspect of the plot to be equal
    ax.set_aspect('equal', 'box')

    # Set the x and y limits to accommodate the circle
    ax.set_xlim(a - radius - 2, a + radius + 2)
    ax.set_ylim(b - radius - 2, b + radius + 2)

    # Add grid and labels for better visualization
    ax.grid(True)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Initial Point and Direction Vector')
    st.pyplot(fig)

# Streamlit app
st.title("Calculus")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page", ["Home", "Partial Derivatives", "Directional Derivatives"])

if page == "Home":
    st.header("Welcome!")
    st.write("""
        We define partial derivatives of a function of the form $f(x,y)$ of two variables $x$ and $y$. We also describe more
             general notion of derivative, called directional derivatives. First of all we look at the mathematical definition
             followed by an opportunity to practice with various functions. In addition, we apply geometric intuition to those 
             concepts. 
    """)

elif page == "Partial Derivatives":
    st.header("Partial Derivatives: $f_x, f_y$")
    st.write("We consider")

    # Input function:
    expr = st.text_input("Enter the function f(x,y) = ", "x**2 + y**2")
    func = sp.sympify(expr)
    x, y = sp.symbols('x y')

    st.latex(r''' f(x,y) =''')
    st.latex(func)

    if st.button("Find $f_x$: "):
        fx = partial_derivative(func, x)
        st.latex(fx)
    if st.button("Find $f_y$: "):
        fy = partial_derivative(func, y)
        st.latex(fy)
    if st.button("Find $f_{xx}$: "):
        fx = partial_derivative(func, x)
        fxx = partial_derivative(fx, x)
        st.latex(fxx)
    if st.button("Find $f_{yy}$: "):
        fy = partial_derivative(func, y)
        fyy = partial_derivative(fy, y)
        st.latex(fyy)
    if st.button("Find $f_{xy}$: "):
        fx = partial_derivative(func, x)
        fxy = partial_derivative(fx, y)
        st.latex(fxy)
    if st.button("Find $f_{yx}$: "):
        fy = partial_derivative(func, y)
        fyx = partial_derivative(fy, x)
        st.latex(fyx)





    
    

elif page == "Directional Derivatives":

    st.subheader('Directional Derivative:')
    st.write('''Let $f(x,y)$ be a function of two variables with domain D. The directional derivative of 
             f at a point (a,b) in the direction given by $v = \langle v_1, v_2\\rangle$''')
    st.write('''The direction vector $v$ should be a unit vector. If is not unit vector, we divide it by its length to get the unit 
             vector with same direction as $v$.''')
    st.latex(r'''u = \frac{v}{|v|} = \langle u_1, u_2\rangle ''')
    st.write('The directional derivative, $f_D(a,b)$ is given by the limit, ')
    st.latex(r'''f_D(a,b) = \lim_{h\rightarrow 0}\frac{f((a,b) + h*u) - f(a,b)}{h} = 
             \lim_{h\rightarrow 0}\frac{f(a+hu_1, b+hu_2) - f(a,b)}{h} ''')
    st.write('if the limit exists')
    
    st.write('After simplification, formula of directional derivative can be written as:')
    st.latex(r'''f_D(a,b) = f_x(a,b)u_1 + f_y(a,b)u_2 = \langle f_x(a,b), f_y(a,b)\rangle.\langle u_1, u_2\rangle''')
    st.write('So the directional derivative at (a,b) is given by the dot product of gradient vector of $f(x,y)$ with unit direction vector.')
    
    st.markdown("""
                - The directional derivative at (a,b) in the direciton $u = <1,0> $ is the partial derivative w.r.t x since
                by substituting $u_1 = 1$, and $u_2 = 0$ in above equation, """)
    st.latex(r""" f_D(a,b) = \lim_{h\rightarrow 0}\frac{f(a+h, b) - f(a,b)}{h} = f_x(a,b).
             """)
    st.markdown("""
                - The directional derivative at (a,b) in the direction $u = <0,1> $ is the partial derivative w.r.t y.
                """)
    st.latex(r""" f_D(a,b) = \lim_{h\rightarrow 0}\frac{f(a, b+h) - f(a,b)}{h} = f_y(a,b).
             """)
    st.markdown("""
            - If the direction vector is given by parameter $\\theta$ and $u = <\cos\\theta, \sin\\theta>$, the directional 
                derivative is given by,
            """)
    st.latex(r"""f_D(a,b) = f_x(a,b)\cos\theta + f_y(a,b)\sin\theta = \langle f_x, f_y \rangle.\langle \cos\theta, \sin\theta \rangle""")
    st.markdown("""
            - If we want to find the directional derivative at a point $(a,b)$ in the direction to another point $(c,d)$, the unit vector 
            is given by, 
             """)
    st.latex(r'''
            u = \frac{\langle c-a, d-b\rangle}{\sqrt{(c-a)^2 + (d-b)^2}}    
            ''')
    col3, col4 = st.columns(2)
    with col3:
        # Display an image from a local file
        st.image("C:/Users/surya/OneDrive/Desktop/Data Science Projects/GradientDescent/directionvector1.png", caption="Direction vector with $\\theta$", use_column_width=True)
    with col4:
        st.image("C:/Users/surya/OneDrive/Desktop/Data Science Projects/GradientDescent/directionvector2.png", caption="Direction vector between two points", use_column_width=True)




    st.markdown('----')
    st.subheader("An Example:")
    st.write('Consider the following function. Find its directional derivative at (1,2) in the direction given by v = <2,1>')
    st.write('The function is:')
    st.latex(r"""f(x,y) = x^2 + xy + y^2""")
    st.write('Find the partial derivatives and evaluate each of them at (1,2): ')
    st.latex(r"""
             \begin{align*}
             f_x &= 2x + y, f_x(1,2) = 2 + 2 = 4\\
             f_y &= x + 2y, f_y(1,2) = 1 + 4 = 5
             \end{align*}
             """)
    
    st.write('Since $v$ is not unit vector, we divide $v$ by its length to get unit vector $u$.')
    st.latex(r"""
             \begin{align*}
             u &= \frac{v}{|v|}\\
              &= \frac{\langle 2,1\rangle}{\sqrt{2^2 + 1}}\\
              &= \langle \frac{2}{\sqrt{5}}, \frac{1}{\sqrt{5}}\rangle
             \end{align*}
            """)
    st.write('The directional derivative of $f(x,y)$ at (1,2) in the direction of $v$ is')
    st.latex(r"""
             \begin{align*}
            f_D(1,2) &= f_x(1,2)u_1 + f_y(1,2)u_2\\
                    &= 4\frac{2}{\sqrt{5}} + 5\frac{1}{\sqrt{5}}\\
                    &= \frac{13}{\sqrt{5}}
             \end{align*}
            """)
    


    st.markdown("--------------------------")

    st.subheader('More Examples:')
    st.write('''Below we consider various functions and practise computing directional derivatives 
    at a point of your choice. You can type in the function you want in the box below, make sure
     it takes in only x and y variables.To enter power such as $x^4$, type x**4, 4x, type 4*x, xy as x*y, 
             sinx as sin(x), $e^x$ as exp(x).''')
    
    # Input function:
    expr = st.text_input("Enter the function f(x,y) = ", "x**2 + y**2")
    func = sp.sympify(expr)
    x, y = sp.symbols('x y')

    st.write('You entered the function $f(x,y)$ = ')
    st.latex(func)


    st.write('Fill in the initial point (a,b) and the terminal point of the direction vector. ')
    col1, col2 = st.columns(2)

    with col1:
        a = st.number_input('Enter the x of initial point(a): ', value = 2)
        b = st.number_input('Enter the y of initial point(b): ', value = 2)

    with col2:
        c = st.number_input('Enter the x of terminal point: ', value = 3)
        d = st.number_input('Enter the y of terminal point: ', value = 3)



    dir = graph_direction(a,b,c,d)
    st.write(dir)



    st.write('Click on the various tabs to display the results:')
    # Input data: 
    if st.button('$f_x = $'):
        FX = partial_derivative(func, x)
        st.latex(FX)
    if st.button('$f_y = $'):
        FY = partial_derivative(func, y)
        st.latex(FY)


    if st.button(f'The gradient vector at ({a},{b}):'):
        FX = partial_derivative(func,x)
        FY = partial_derivative(func,y)
        eval_fx = funct_eval(FX, (a,b))
        eval_fy = funct_eval(FY, (a,b))
        st.write(f'= $\langle$ {eval_fx}, {eval_fy}$\\rangle$')


    # Find the derivative:
    if st.button(f'Directional Derivative at ({a},{b}):'):
        dd, G, V = direct_derivative(func, (a,b), (c,d))
        DD = round(dd,2)
        st.write(f' = {DD}')
    

# Run the app with: streamlit run app.py


