package TP2.ex3.ex3_2;

public class Employe {
    static int idstatic=0;
    private int id;
    private String firstname;
    private String lastname;
    private int age;
    private float salaire;
    public Employe(String firstname, String lastname, int age, float salaire) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.age = age;
        this.salaire = salaire;
        idstatic++;
        id=idstatic;

    }
    public String getAge() {
        return Integer.toString(age);
    }
    public String getFirstname() {
        return firstname;
    }
    public String getLastname() {
        return lastname;
    }
    public String getSalaire() {
        return Float.toString(salaire);
    }
    public String getId() {
        return Integer.toString(id);
    }
}
