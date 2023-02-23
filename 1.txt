using UnityEngine;

public class PlayerController : MonoBehaviour {
    public float speed = 10.0f;
    public GameObject bulletPrefab;
    public Transform bulletSpawn;

    private float fireRate = 0.5f;
    private float nextFire = 0.0f;

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
}
