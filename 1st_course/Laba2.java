/*
Автор: Потанин Лев Антонович
Группа: R3141
Вариант: 521
Оценка: 10 баллов
*/

import ru.ifmo.se.pokemon.*;

public class Laba2 {
    public static void main(String[] args) {
        Battle b = new Battle();
        Pokemon p1 = new Heatmor("Sweet");
        Pokemon p2 = new Tyrunt("Dreams");
        Pokemon p3 = new Tyrantrum("Are");
        Pokemon p4 = new Axew("Made");
        Pokemon p5 = new Fraxure("Of");
        Pokemon p6 = new Haxorus("This");
        b.addAlly(p1);
        b.addAlly(p2);
        b.addAlly(p3);
        b.addFoe(p4);
        b.addFoe(p5);
        b.addFoe(p6);
        b.go();
    }
}

class Heatmor extends Pokemon {
    Heatmor(String name) {
        super(name, 25);
        double hp = 85, attack = 97, defense = 66, special_attack = 105, special_defense = 66, speed = 65;
        setStats(hp, attack, defense, special_attack, special_defense, speed);
        setType(Type.FIRE);
        setMove(new Bulldoze(), new Work_Up(), new Pound(), new Shadow_Ball());
    }
}
class Tyrunt extends Pokemon {
    Tyrunt(String name) {
        super(name, 25);
        double hp = 58, attack = 89, defense = 77, special_attack = 45, special_defense = 45, speed = 48;
        setStats(hp, attack, defense, special_attack, special_defense, speed);
        setType(Type.ROCK, Type.DRAGON);
        setMove(new Confide(), new Facade(), new Splash());
    }
}
class Tyrantrum extends Tyrunt {
    Tyrantrum(String name) {
        super(name);
        double hp = 82, attack = 121, defense = 119, special_attack = 69, special_defense = 59, speed = 71;
        setStats(hp, attack, defense, special_attack, special_defense, speed);
        setType(Type.ROCK, Type.DRAGON);
        setMove(new Confide(), new Facade(), new Splash(), new Psybeam());
    }
}
class Axew extends Pokemon {
    Axew(String name) {
        super(name, 25);
        double hp = 46, attack = 87, defense = 60, special_attack = 30, special_defense = 40, speed = 57;
        setStats(hp, attack, defense, special_attack, special_defense, speed);
        setType(Type.DRAGON);
        setMove(new Confide(), new Facade());
    }
}
class Fraxure extends Axew {
    Fraxure(String name) {
        super(name);
        double hp = 66, attack = 117, defense = 70, special_attack = 40, special_defense = 50, speed = 67;
        setStats(hp, attack, defense, special_attack, special_defense, speed);
        setType(Type.DRAGON);
        setMove(new Confide(), new Facade(), new Air_Cutter());
    }
}
class Haxorus extends Fraxure {
    Haxorus(String name) {
        super(name);
        double hp = 76, attack = 147, defense = 90, special_attack = 60, special_defense = 70, speed = 97;
        setStats(hp, attack, defense, special_attack, special_defense, speed);
        setType(Type.DRAGON);
        setMove(new Confide(), new Facade(), new Air_Cutter(), new Swagger());
    }
}


class Confide extends StatusMove {
    Confide() {
        super(Type.NORMAL, 0.00d, 0.00d);
    }
    @Override
    protected void applyOppEffects (Pokemon p) {
        p.setMod(Stat.SPECIAL_ATTACK, -1);
    }
}
class Facade extends PhysicalMove {
    Facade() {
        super(Type.NORMAL, 70, 1);
    }
}
class Swagger extends PhysicalMove {
    Swagger() {
        super(Type.NORMAL, 0, 0.85);
    }
    @Override
    protected void applyOppEffects (Pokemon p) {
        p.setMod(Stat.ATTACK, -2);
    }
}
class Work_Up extends StatusMove {
    Work_Up() {
        super();
    }
    @Override
    protected void applyOppEffects (Pokemon p) {
        p.setMod(Stat.SPECIAL_ATTACK, 1);
        p.setMod(Stat.ATTACK, 1);
    }
}
class Pound extends PhysicalMove {
    Pound() {
        super(Type.NORMAL, 40, 1);
    }
}
class Splash extends PhysicalMove {
    Splash() {
        super(Type.NORMAL, 0, 1000);
    }
}
class Bulldoze extends SpecialMove {
    Bulldoze() {
        super(Type.GROUND, 60, 1);
    }
    protected void applyOppEffects (Pokemon p) {
        p.setMod(Stat.SPEED, -1);
    }
}
class Shadow_Ball extends SpecialMove {
    Shadow_Ball() {
        super(Type.GHOST, 80, 1);
    }
}
class Psybeam extends SpecialMove {
    Psybeam() {
        super(Type.PSYCHIC, 65, 1);
    }
    @Override
    protected void applyOppEffects (Pokemon p) {
        if (Math.random()<=0.1)p.confuse();
    }
}
class Air_Cutter extends SpecialMove {
    Air_Cutter() {
        super(Type.FLYING, 60, 0.95);
    }
}
