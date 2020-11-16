public static boolean whilestmt(String s){
    x = getNextToken(s)
    if(x == whilest){
        x = getNextToken(s);
        if(x == leftparenthasis){
            x = getNextToken(s);
            if(x == boolstmt){
                x = getNextToken(s);
                if(x == rightparenthasis){
                    x = getNextToken(s);
                    if(x == opencurl){
                        x = getNextToken(s);
                        if(x == opencurl){  
                            x = getNextToken(s);
                            if(x == blockstmt)(){
                                x = getNextToken(s);
                                if(x == closecurl){
                                    return true;
                                }else{
                                    return false;
                                }
                            }else{
                                return false;
                            }
                        }else{
                            return false;
                        }
                    }else{
                        return false;
                    }
                }else{
                    return false;
                }
            }else{
                return false;
            }
        }else{
            return false;
        }
    }else{
        return false;
    }
}

//assume getNextToken pops string stack based on spaces.
public static boolean ifstmt(String s){
    x = getNextToken(s);
    if(x == ifst){
        x = getNextToken(s);
        if(x == leftparenthasis){
            x = getNextToken(s);
            if(x == boolstmt){
                x = getNextToken(s);
                if(x == rightparenthasis){
                    x = getNextToken(s);
                    //check if stmt or opencurl
                    if(x == stmt || x == opencurl){
                        //if open curl check for close
                        if(x == opencurl){
                            x = getNextToken(s);
                            if(x == block){
                                x = getNextToken(s);
                                if(x == closecurl){
                                    if(s != " " || s != ""){
                                        check_for_else_or_elseif_stmt(s);
                                    }else{ return true; }
                                }else{ return false; }
                            }else{ return false; }
                        }else if(s != " " || s != ""){
                            check_for_else_or_elseif_stmt(s);
                        }else{ return true; }
                    }else{ return false; }
                }else{ return false; }
            }else{ return false; }
        }else{ return false; }
    }else{ return false; }
}

public static boolean check_for_else_or_elseif_stmt(String s){
    x = getNextToken(s);
    if(x == else_stmt){
        x = getNextToken(s);
        if(x == if_stmt){
            //concatenates popped with string and rechecks if statment
            x = x + " " + s;
            return if_stmt(s);
        }else if (x == stmt || x == opencurl){
            x = getNextToken(s);
                if(x == block){
                    x = getNextToken(s);
                    if(x == closecurl){
                        if(s != " " || s != ""){
                            ifstmt(s);
                        }else{ return true; }
                    }else{ return false; }
                }else{ return false; }
            return true;
        }else {return false;}
    }else{ return false;}
}

public static boolean assignstmt(String s){
    x = getNextToken(s);
    if(x == var){
        x = getNextToken(s);
        if(x == equalsign){
            x = getNextToken(s);
            if(x == var || x == var[mem || x == const || x == func || x == null]){
                return true;
            }else { return false; }
        }else { return false; }
    }else { return false; }
}

//assume getNextToken pops string stack based on spaces.
public static boolean mathexpr(String s){
    x = getNextToken(s);
    if(x == var){
        x = getNextToken(s);
        if(x == op){
            x = getNextToken(s);
            if(x == math_expr){
                return math_expr(x + " " + s);
            }else if(x == var){
                return true;
            }else { return false; }
        }else { return false; }
    }else { return false; }
}