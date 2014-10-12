class Atom(CallX):
    def unify (self, other, frame, occurs_check=False):
        if isinstance (other, Var):
            return other.unify(self,frame,occurs_check)
        elif isinstance (other, Atom):
            if other.name != self.name:
                raise UnificationFailed
            return
        raise UnificationFailed
    unify._annspecialcase_="specialize:arg(3)"

class AndContinuation(engine.Continuation):
    def _init_(self, next_call, continuation):
        self.next_call = next_call
        self.continuation = continuation

    def call(self, engine):
        next_call = self.next_call.dereference(engine.frame)
        return engine.call(next_call, self.continuation)
    def impl_and(engine, call1, call2, continuation):
        and_continuation = AndContinuation(call2, continuation)
        return engine.call (call1, and_continuation)

def impl_between(engine, lower, upper, varorint, continuation):
    oldstate = engine.frame.branch()
    for i in range (lower, upper):
        try:
            varorint.unify (Number(i), engine.frame)
            return continuation.call(engine)
        except error.UnificationFailed:
            engine.frame.revert (oldstate)
    varorint.unify(Number(upper), engine.frame)
    return continuation.call(engine)
expose_builtin(impl_between, "between", unwrap_spec=["int", "int", "obj"], handles_continuation=True)

def impl_setitem_hashmap(engine, hashmap, key, value, continuation):
    old=hashmap.setitem(key, value)
    try:
        return continuation.call(engine)
    except error.UnificationFailed:
        hashmap.setitem(key, old)
        raise
expose_builtin (impl_setitem_hashmap, "setitem_hashmap", unwrap_spec=["obj", "atom", "obj"], handles_continuation=True)

def who_won():
    global game_ended
    try:
        How = term.Var(0)
        query = wrap (("end_state", [usermoves,computermoves], How))
        engine.run(query)
        game_ended = True
        return unwrap (How, engine)
    except UnificationFailed:
        return False
    
        
    
