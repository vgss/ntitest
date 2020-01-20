package br.ufpe.nti.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/admin")
public class AdminController {

    @RequestMapping
    public String viewManageUsers() {
        return "/admin/manage-users";
    }
}
