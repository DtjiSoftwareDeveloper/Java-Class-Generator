
public class Digimon {

    private String name; 

    private double maxHP; 

    private double attackPower; 

    private double defense; 

    public Digimon(){
    
    }     

    public Digimon(String name, double maxHP, double attackPower, double defense){
        
        this.name = name;

        this.maxHP = maxHP;

        this.attackPower = attackPower;

        this.defense = defense;

    }        

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getMaxHP() {
        return maxHP;
    }

    public void setMaxHP(double maxHP) {
        this.maxHP = maxHP;
    }

    public double getAttackPower() {
        return attackPower;
    }

    public void setAttackPower(double attackPower) {
        this.attackPower = attackPower;
    }

    public double getDefense() {
        return defense;
    }

    public void setDefense(double defense) {
        this.defense = defense;
    }

        
}
