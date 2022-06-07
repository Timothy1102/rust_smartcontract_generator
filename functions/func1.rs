pub fn update_list(&mut self, acc: String, amount: u128) {
    if self.account_list.get(&acc).is_some() {
        let old_vol = self.account_list.remove(&acc).unwrap();
        let current_vol = amount.checked_add(old_vol).unwrap();
        self.account_list.insert(&acc, &current_vol);
        // update top_accounts
        if self.top_accounts.len() < 3 {
            let old_vol = self.top_accounts.remove(&acc).unwrap();
            let current_vol = amount.checked_add(old_vol).unwrap();
            self.top_accounts.insert(&acc, &current_vol);
        } else {
            if self.top_accounts.get(&acc).is_some() {
                let old_vol = self.top_accounts.remove(&acc).unwrap();
                let current_vol = amount.checked_add(old_vol).unwrap();
                self.top_accounts.insert(&acc, &current_vol);
            } else {
                let minacc = Contract::minacc(&self);
                let minaccount = minacc.0;
                let min_bal = minacc.1;
                if current_vol > min_bal {
                    self.top_accounts.remove(&minaccount);
                    self.top_accounts.insert(&acc, &current_vol);
                }
            }
        }
    } else {
        self.account_list.insert(&acc, &amount);
        if self.top_accounts.len() < 3 {
            self.top_accounts.insert(&acc, &amount);
        } else {
            let minacc = Contract::minacc(&self);
            let minaccount = minacc.0;
            let bal = minacc.1;
            if amount > bal {
                self.top_accounts.remove(&minaccount);
                self.top_accounts.insert(&acc, &amount);
            }
        }
    }
}