class BaseApiTest:
    def test_required(self):
        self.client.force_login(user=self.admin)

        res = self.client.post(self.url, self.request)
        self.assertEqual(res.status_code, 201)

        for k in self.request.keys():
            req = self.request.copy()
            req.pop(k)
            res = self.client.post(self.url, req)
            self.assertEqual(res.status_code, 400 if k in self.required else 201, k)

    def test_validation(self):
        self.client.force_login(user=self.admin)

        for p in self.non_valid:
            req = self.request.copy()
            req[p[0]] = p[1]
            res = self.client.post(self.url, req)
            self.assertEqual(res.status_code, 400, p)

    def auth_test(self, url, list, retrieve, create, update, destroy):
        res = self.client.get(url)
        self.assertEqual(res.status_code, list)

        res = self.client.get(url + "1/")
        self.assertEqual(res.status_code, retrieve)

        res = self.client.post(url)
        self.assertEqual(res.status_code, create)

        res = self.client.put(url + "1/")
        self.assertEqual(res.status_code, update)

        res = self.client.delete(url + "1/")
        self.assertEqual(res.status_code, destroy)
