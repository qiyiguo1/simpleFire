using UnityEngine;
using UnityEngine.UI;

public class PlayerController : MonoBehaviour {
    public float speed = 10.0f;
    public GameObject bulletPrefab;
    public Transform bulletSpawn;
    public int startingHealth = 100;
    public Text healthText;

    private int currentHealth;
    private float fireRate = 0.5f;
    private float nextFire = 0.0f;

    void Start() {
        currentHealth = startingHealth;
        healthText.text = "Health: " + currentHealth;
    }

    void Update() {
        float horizontal = Input.GetAxis("Horizontal");
        float vertical = Input.GetAxis("Vertical");

        transform.Translate(new Vector3(horizontal, 0, vertical) * speed * Time.deltaTime);

        if (Input.GetButton("Fire1") && Time.time > nextFire) {
            nextFire = Time.time + fireRate;
            Fire();
        }
    }

    void Fire() {
        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().velocity = bullet.transform.forward * 20;
        Destroy(bullet, 2.0f);
    }

    void OnTriggerEnter(Collider other) {
        if (other.gameObject.CompareTag("Enemy")) {
            currentHealth -= 10;
            healthText.text = "Health: " + currentHealth;

            if (currentHealth <= 0) {
                Destroy(gameObject);
            }
        }
    }
}
using UnityEngine;

public class EnemyController : MonoBehaviour {
    public int health = 50;
    public GameObject bulletPrefab;
    public Transform bulletSpawn;

    private float fireRate = 1.0f;
    private float nextFire = 0.0f;

    void Update() {
        GameObject player = GameObject.FindGameObjectWithTag("Player");

        if (player != null && Time.time > nextFire) {
            nextFire = Time.time + fireRate;
            Fire(player.transform.position);
        }
    }

    void Fire(Vector3 target) {
        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().velocity = (target - bullet.transform.position).normalized * 20;
        Destroy(bullet, 2.0f);
    }

    void OnTriggerEnter(Collider other) {
        if (other.gameObject.CompareTag("Bullet")) {
            health -= 10;

            if (health <= 0) {
                Destroy(gameObject);
            }
        }
    }
}
using UnityEngine;

public class EnemyController : MonoBehaviour {
    public int health = 50;
    public GameObject bulletPrefab;
    public Transform bulletSpawn;

    private float fireRate = 1.0f;
    private float nextFire = 0.0f;

    void Update() {
        GameObject player = GameObject.FindGameObjectWithTag("Player");

        if (player != null && Time.time > nextFire) {
            nextFire = Time.time + fireRate;
            Fire(player.transform.position);
        }
    }

    void Fire(Vector3 target) {
        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().velocity = (target - bullet.transform.position).normalized * 20;
        Destroy(bullet, 2.0f);
    }

    void OnTriggerEnter(Collider other) {
        if (other.gameObject.CompareTag("Bullet")) {
            health -= 10;

            if (health <= 0) {
                Destroy(gameObject);
            }
        }
    }
}
using UnityEngine;

public class EnemyController : MonoBehaviour {
    public int health = 50;
    
   
public GameObject bulletPrefab;
    
   
public Transform bulletSpawn;

    

   


private float fireRate = 1.0f;
    
   
private float nextFire = 0.0f;

    

   


void Update() {
        GameObject player = GameObject.FindGameObjectWithTag(
        GameObject player = GameObject.FindGameObjectWithTag
"Player");

        

       
if (player != null && Time.time > nextFire) {
            nextFire = Time.time + fireRate;
            Fire(player.transform.position);
        }
    }

    
            nextFire = Time.time + fireRate;
            Fire(player.transform.position);
       

            nextFire = Time.time + fireRate;
            Fire(player.transform.position);

            nextFire = Time.time + fireRate;
            Fire(player.transform

            nextFire = Time.time + fireRate;
            Fire(player

            nextFire = Time.time + fireRate;

            nextFire = Time.time + fireRate

            nextFire = Time

            nextFire =

            next
void Fire(Vector3 target) {
        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().velocity = (target - bullet.transform.position).normalized * 
        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().velocity = (target - bullet.transform.position).normalized * 

        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().velocity = (target - bullet.transform.position).normalized *

        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().velocity = (target - bullet.transform.position).normalized

        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().velocity = (target - bullet.transform.position).

        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().velocity = (target - bullet.transform.position

        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().velocity = (target - bullet

        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().velocity = (target - 

        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().velocity = (

        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().velocity =

        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().velocity

        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation);
        bullet.GetComponent<Rigidbody>().

        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn.rotation

        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, bulletSpawn

        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position, 

        GameObject bullet = Instantiate(bulletPrefab, bulletSpawn.position,

        GameObject bullet = Instantiate(bulletPrefab, bullet

        GameObject bullet = Instantiate(bulletPrefab, 

        GameObject bullet = Instantiate(bulletPrefab,

        GameObject bullet = Instantiate(bullet

        GameObject bullet = Instantiate(b

        GameObject bullet

        GameObject 
20;
        Destroy(bullet, 
        Destroy(bullet, 

        Destroy(bullet

        Destroy(b

       
2.0f);
    }

    
   
void OnTriggerEnter(Collider other) {
        
       
if (other.gameObject.CompareTag("Bullet")) {
            health -= 
            health -= 

            health -=
10;

            if (health <= 0) {
                Destroy(gameObject);
            }
        }
    }
}

                Destroy(gameObject