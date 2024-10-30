class MyQueue {
public:
    stack<int> main; 
    stack<int> aux;
    MyQueue() {
        
    }
    
    void push(int x) {
        while(!main.empty()){
            aux.push(main.top());
            main.pop();
        }
        main.push(x);
        while(!aux.empty()){
            main.push(aux.top());
            aux.pop();
        }
    }
    
    int pop() {
        int x = main.top();
        main.pop();
        return x;
    }
    
    int peek() {
        return main.top();
    }
    
    bool empty() {
        return main.empty();
    }
};

/