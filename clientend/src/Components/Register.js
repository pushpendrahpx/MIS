import React, { Component } from 'react'
import { Form,
         Button,
         Jumbotron,
         Container,
         Row,
         Col
} from 'react-bootstrap'

export default class Login extends Component {
    constructor(props){
        super(props)

        this.state = {
            email:"",
            password:""
        }
    }

    login = (event)=>{
        event.preventDefault();

        console.log(event.target)
    }

    render() {
        return (
            <Jumbotron style={{margin:'20px'}}>
  <h1 style={{textAlign:"center"}}>REGISTER FORM</h1>
  
 <Container>
     <Row>
         <Col><Form onSubmit={this.login}>
            <Form.Group controlId="formBasicEmail">
                    <Form.Label>Email address</Form.Label>
                    <Form.Control type="email" placeholder="Enter Email" />
                    <Form.Text className="text-muted">
                    We'll never share your email with anyone else.
                    </Form.Text>
                </Form.Group>

                <Form.Group controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                    <Form.Control type="password" placeholder="Password" />
                </Form.Group>
                <Form.Group controlId="formBasicCheckbox">
                    <Form.Check type="checkbox" label="Remember Me" />
                </Form.Group>
                <Button variant="primary" type="submit">
                    Submit
                </Button>
                </Form>

         </Col>
     </Row>
 </Container>
</Jumbotron>
            
        )
    }
}
