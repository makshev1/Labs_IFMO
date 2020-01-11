class Smoker extends Human implements Feel, Brush, Call {
    Smoker(String name) {
        this.name = name;
    }

    @Override
    public void brush_off(Status status) {
        System.out.print(getName() + " brush off " + status + " ");
    }

    @Override
    public void call_for(Human whom) {
        System.out.print(getName() + " call for " + whom.getName() + " ");
    }

    @Override
    public void feel(Status status) {
        System.out.print(getName() + " felt " + status + " ");
    }

    @Override
    public String toString(){
        return ("Class: Smoker; Name: " + name);
    }
}
