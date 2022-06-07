pub fn get_top(&self) -> (String, String, String) {
    let mut iter = self.top_accounts.iter();
    let len = self.top_accounts.len();
    // "default" means that position doesn't contain an account (total user < 3).
    let acc1 = String::from("default");
    let acc2 = String::from("default");
    let acc3 = String::from("default");
    let mut tup: (String, String, String) = (acc1, acc2, acc3);
    for i in 0..len {
        let next = iter.next().unwrap();
        if i == 0 {
            tup.0 = next.0;
        } else if i == 1 {
            tup.1 = next.0;
        } else if i == 2 {
            tup.2 = next.0;
        }
    }
    tup
}